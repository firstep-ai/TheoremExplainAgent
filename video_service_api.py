from fastapi import FastAPI
from pydantic import BaseModel
import os
import asyncio
import uuid
from datetime import datetime

app = FastAPI()

class VideoRequest(BaseModel):
    topic: str
    context: str

async def stream_subprocess_output(process, log_file_path):
    """异步打印子进程的输出并写入日志文件"""
    async def _read_stream(stream, name):
        while True:
            line = await stream.readline()
            if line:
                decoded_line = line.decode().rstrip()
                log_line = f"[{name}] {decoded_line}"
                print(log_line)

                with open(log_file_path, "a", encoding="utf-8") as f:
                    f.write(log_line + "\n")
            else:
                break

    await asyncio.gather(
        _read_stream(process.stdout, "STDOUT"),
        _read_stream(process.stderr, "STDERR"),
    )

@app.post("/generate_video")
async def generate_video(request: VideoRequest):
    print("生成视频的项目接收到 transfer_protocol 的请求参数:", request)
    
    session_id = str(uuid.uuid4())
    output_dir = f"output/{session_id}"
    os.makedirs(output_dir, exist_ok=True)

    # 日志文件路径
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(output_dir, f"generate_log_{timestamp}.txt")

    # 构建命令
    command = f'python generate_video.py --model "openai/o3-mini" --helper_model "openai/o3-mini" ' \
              f'--output_dir "{output_dir}" --topic "{request.topic}" --context "{request.context}"'

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # 实时打印 + 写日志
    await stream_subprocess_output(process, log_file_path)

    await process.wait()

    if process.returncode == 0:
        file_prefix = request.topic.replace(" ", "_")
        video_path = f"{output_dir}/{file_prefix}/{file_prefix}_combined.mp4"
        return {
            "message": "Video generation successful",
            "video_path": video_path,
            "log_file": log_file_path
        }
    else:
        return {
            "message": "Video generation failed",
            "error": f"Process exited with code {process.returncode}",
            "log_file": log_file_path
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
