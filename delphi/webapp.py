from fasthtml.common import *
import pypsa

n = pypsa.Network()
comps = [*n.component_attrs.keys()]
attrs = {k:[*n.component_attrs[k].index] 
           for k in n.component_attrs.keys()}

app,rt = fast_app(live=True)

def mk_opts(nm,opts):
    return (Option(f'Select {nm}', disabled=True, selected=True),
            *[Option(o) for o in opts])

@app.get('/get_subs')
def get_sub(choice:str):
    attrs = [*attrs[choice]]
    return Select(*mk_opts('attribute',attrs),name="attrs")

@app.get("/")
def homepage(): 
    comp_drop = Select(
        *mk_opts('component',comps),
        name='component',
        hx_get='/get_subs', hx_target='#subelements')
    
    return Titled('Electric!',
                  Div(
                      Label("Component:",for_="component"),
                      comp_drop),
                  Div(Label("Attribute", for_="attrs"),
                      Div(id='subelements')))                 



serve()