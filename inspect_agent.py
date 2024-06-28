import llama_index.core.agent as agent

def inspect_module(module):
    print(f"Inspecting {module.__name__} module:")
    for attribute_name in dir(module):
        print(attribute_name)

inspect_module(agent)
