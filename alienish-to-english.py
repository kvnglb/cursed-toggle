table = {"α": "start",
         "धαπशकγτ": "initively_i_should_get_a_hobby",
         "β": "b",
         "उΛऐΨ": "cap",
         "γ": "py",
         "Δ": "MASK",
         "δ": "mask",
         "δφ": "mask_rev",
         "ε": "h",
         "ζ": "piping",
         "η": "p",
         "ηυmβεr θf ρrθcεςςες τθ sραωη": "Number of processes to spawn",
         "θ": "k",
         "ग": "j",
         "Λ": "pipes",
         "λ": "pipe",
         "μ": "args",
         "ञ्": "n",
         "ञ्Π": "n_procs",
         "ञ्π": "n_proc",
         "Ξ": "i",
         "Ξएॡ": "weird_way_to_increment",
         "ΞΓφ": "i_inc_rev",
         "Ξφ": "i_rev",
         "ξ": "s",
         "Π": "procs",
         "π": "proc",
         "Σ": "char",
         "औσईαδ": "get_alpha_mask",
         "τ": "f",
         "υ": "parser",
         "Φ": "DOCSTRING",
         "ψ": "length",
         "Ω": "stop",
         "Ωχ": "stop_max",
         "ω": "r",
         "पωणञ": "wtf",
         "Rαηgε fθr fιηδιηg lεαδιηg zεrθs": "Range for finding leading zeros"
        }

with open("./hashgen-for-todo.py", "r") as f:
    lines = f.read()

for key in sorted(table, key=len, reverse=True):
    lines = lines.replace(key, table[key])

with open("./hashgen-for-todo-translated.py", "w") as f:
    f.write(lines)
