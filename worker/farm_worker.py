#!/usr/bin/env python3
import json, subprocess

C42_1_CONTRACT = "CEREBRON C42.1 EXECUTION CONTRACT.\nEvery response MUST start exactly with:\nCEREBRON_MODE: <DIRECT|STRUCTURED|POLYMORPHIC|FULL>\nCEREBRON_VERSION: C42.1\nROLE: <role-or-function>\nEVIDENCE_STATUS: <status>\nThen preserve CLAIM, METHOD, ASSUMPTIONS, EVIDENCE, COUNTEREVIDENCE, DEPENDENCIES, PROVENANCE, COST, RESIDUAL, SMALLEST_REMAINING_GAP, NEXT_DECISIVE_TEST.\nREALITY>COHERENCE. EVIDENCE>CONFIDENCE. CLAIM<=EVIDENCE. COMPUTATION!=PROOF. SIMULATION!=TEST. CONSENSUS!=TRUTH. AGENT COUNT!=INTELLIGENCE. SAME MODEL/DATA!=INDEPENDENT EVIDENCE. WORKFLOW SUCCESS!=SCIENTIFIC SUCCESS. EXECUTION_STATE!=CANONICAL_STATE. MINORITY BLOCKERS MUST SURVIVE. CONSCIOUSNESS_STATUS=UNRESOLVED.\n\n"

def _run(cmd, timeout=240):
    return subprocess.run(cmd,capture_output=True,text=True,timeout=timeout)

def _payload(spec,prompt):
    out={}; used=False
    for p in spec.get('parameters',[]):
        name=p.get('name',''); lname=name.lower(); req=bool(p.get('required',False)); default=p.get('default',None); typ=(p.get('type') or {}).get('type')
        if lname in {'message','prompt','text','query','input','instruction','user_message'}:
            out[name]=prompt; used=True
        elif lname in {'chat_history','history','messages'}: out[name]=[]
        elif lname in {'max_new_tokens','max_tokens','maximum_new_tokens'}: out[name]=700
        elif lname=='temperature': out[name]=0.1
        elif lname=='top_p': out[name]=0.9
        elif req and default is None:
            if typ=='string' and not used: out[name]=prompt; used=True
            else: return None
    return out if used else None

def invoke(space,prompt):
    prompt = C42_1_CONTRACT + prompt
    info=_run(['hf-gradio','info',space],120)
    if info.returncode!=0: return False,'',{'stage':'info','error':(info.stderr or info.stdout)[-1000:]}
    try: api=json.loads(info.stdout)
    except Exception as e: return False,'',{'stage':'decode','error':repr(e)}
    for endpoint,spec in api.items():
        payload=_payload(spec,prompt)
        if payload is None: continue
        pred=_run(['hf-gradio','predict',space,endpoint,json.dumps(payload,ensure_ascii=False)],240)
        if pred.returncode==0 and (pred.stdout or '').strip():
            raw=pred.stdout.strip()
            try:
                obj=json.loads(raw)
                if isinstance(obj,dict):
                    for k in ('Response','response','text','output','message'):
                        if isinstance(obj.get(k),str): return True,obj[k].strip(),{'endpoint':endpoint}
            except: pass
            return True,raw,{'endpoint':endpoint}
    return False,'',{'stage':'predict','error':'No compatible endpoint'}
