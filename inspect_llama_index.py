import llama_index
import pkgutil

package = llama_index

print(f"Inspecting {package.__name__} package:")
for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
    print(f"Module: {modname}, Is Package: {ispkg}")
