

# def load_jobs_from_db():
#     with engine.connect() as conn:
#         result = conn.execution_options(stream_results=True).execute(text("select * from jobs"))
#         result_all = result.all()
#         return result_all