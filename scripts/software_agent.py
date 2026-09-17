import json, os
from pathlib import Path
from hf_gradio import GradioClient
role=os.environ['ROLE']; model=os.environ['MODEL']; focus=os.environ.get('FOCUS','')
prompt=f'''You are role {role} in CEREBRON Farm 17 Computing Software.
Focus: {focus}
Work as a software/computing specialist. Distinguish design, implementation, test, benchmark, deployment and production evidence. Do not invent executions. Identify assumptions, failure modes, security risks, observability needs and measurable validation steps. Return concise sections: FINDINGS, EVIDENCE, RISKS, TESTS, UNKNOWN, VERDICT.'''
out={'role':role,'model':model,'focus':focus,'success':False,'result':None,'error':None}
try:
    c=GradioClient(model)
    r=c.predict(message=prompt, api_name='/chat')
    out['success']=True; out['result']=r
except Exception as e: out['error']=repr(e)
Path('out').mkdir(exist_ok=True)
Path(f'out/{role}.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))