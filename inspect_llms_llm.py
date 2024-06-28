import llama_index.core.llms.llm as llm
import pkgutil

def inspect_package(package):
    print(f"Inspecting {package.__name__} package:")
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        print(f"Module: {modname}, Is Package: {ispkg}")

inspect_package(llm)
