# from fastapi import FastAPI, Request


# app = FastAPI()

# @app.middleware("http")
# async def my_middleware(request: Request, call_next):

#    print("before request, inside middleware")

#    response = await call_next(request)
#    print(response)
   
#    print("after request, inside middleware")
#    return response



# @app.get('/')
# def root():
#     return "all good"


# @app.get('/health')
# def health():
#     return "all good health"


# import time
# from fastapi import FastAPI, Request

# app = FastAPI()


# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)          # this actually runs the endpoint
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     print(f"⏱️ {request.method} {request.url.path} took {process_time:.4f}s")
#     return response


# from fastapi import FastAPI, Request
# import logging

# app = FastAPI()

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("api")

# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     logger.info(f"📥 Incoming request: {request.method} {request.url.path}")
#     response = await call_next(request)
#     logger.info(f"📤 Response status: {response.status_code}")
#     return response



# @app.get('/health')
# def health():
#     return "all good health"

# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

# app = FastAPI()

# @app.middleware("http")
# async def check_api_key(request: Request, call_next):
#     if request.url.path.startswith("/admin") and request.headers.get("X-API-Key") != "secret-key":
#         return JSONResponse(status_code=403, content={"error": "Missing or invalid API key"})
#     return await call_next(request)

# @app.get('/admin/health')
# def health():
#     return "all good health"

