import argparse
import hashlib
from multiprocessing import Process, Pipe
import os
import time


def धαπशकγτ(ψ):
    return bytearray(f"""import hashlib


def cursed_toggle(b: bool) -> bool:
    \"\"\"Toggle the boolean input `b`.\"\"\"
    if type(b) is not bool:
        raise TypeError("Argument `b` must be Boolean.")

    return bool(_cursed_toggle(b))


def _cursed_toggle(b: bool) -> complex:
    \"\"\"I<DOCSTRING>.

    \"\"\"
    with open(__file__, "r") as f:
        h = int(hashlib.sha256(f.read().encode("ascii")).hexdigest()[:{ψ}], 16)
    return 1 - b + h
""", "ascii")

def उΛऐΨ(ξ, δ):
    β, ग = bin(δ)[2:].zfill(len(ξ)), 0
    for Ξ in β:
        if Ξ == "1":
            ξ[ग] = ord(chr(ξ[ग]).upper())
        ग += 1
    return ξ

def Ξएॡ(Ξ, δ):
    Ξφ = bin(Ξ)[::-1][:-2]
    δφ = bin(δ)[::-1][:-2]
    ग, θ, ΞΓφ = 0, 0, ""
    while ग < len(Ξφ):
        if δφ[θ] == "0":
            ΞΓφ += "0"
        else:
            ΞΓφ += Ξφ[ग]
            ग += 1
        θ += 1
    return int(ΞΓφ[::-1], 2)

def औσईαδ(ξ):
    δ = 0
    for Σ in ξ:
        δ = δ << 1 | chr(Σ).isalpha()
    return δ

def पωणञ(ψ, ञ्π, ञ्Π, η):
    Ωχ = 2**len(bin(Δ).replace("0", "")[1:])
    ञ् = (Ωχ // (ञ्Π+1)) + 1
    α, Ω = ञ्π * ञ्, (ञ्π + 1) * ञ्
    Ξ, ग = α, Ξएॡ(α, Δ)
    while Ξ < Ω:
        ξ = उΛऐΨ(Φ[:].lower(), ग)
        γ = धαπशकγτ(ψ).replace(b"<DOCSTRING>", ξ)
        ε = hashlib.sha256(γ).hexdigest()
        if int(ε[:ψ], 16) == 0:
            η.send([γ.decode("ascii"), ε])
            return
        if Ξ % 10000000 == 0:
            print(ञ्π, Ξ)
        Ξ += 1
        try:
            ग = Ξएॡ(Ξ, Δ)
        except IndexError:
            break
    η.send([None, None])


Φ = bytearray("""mplement the core of the cursed_toggle function.

    Main part is excluded for proper testing. Behaviour of the function should be
        f(1) -> 0
        f(0) -> 1
    But with a bool conversion in the return, it would be sufficient that
        f(1) -> 0
        f(0) -> anything but 0
    because bool(5), bool(-2), etc. will result in True.

    Well, there shouldn't be much of an explanation. This is trivial and
    self-explanatory. Somehow, this thing fails when checking out on windows.
    TODO: This should be fixed. But be careful, this .py file is very, very
    fragile""", "ascii")

Δ = औσईαδ(Φ)


if __name__ == "__main__":
    υ = argparse.ArgumentParser()
    υ.add_argument("-ञ्", "--ञ्Π", type=int, required=True, help="ηυmβεr θf ρrθcεςςες τθ sραωη.")
    υ.add_argument("-ω", type=int, required=True, nargs="+", help="Rαηgε fθr fιηδιηg lεαδιηg zεrθs.")
    μ = υ.parse_args()

    for ψ in range(μ.ω[0], μ.ω[1]):
        print(f"LENGTH: {ψ}")
        print("=================")

        Π, Λ = [], []
        for ञ्π in range(μ.ञ्Π):
            Λ.append(Pipe(False))
            Π.append(Process(target=पωणञ, args=(ψ, ञ्π, μ.ञ्Π-1, Λ[ञ्π][1]), daemon=True))
            Π[ञ्π].start()

        ζ, Ξ = True, 0
        while ζ and Ξ < μ.ञ्Π:
            for λ in Λ:
                η = λ[0]
                if η.poll():
                    γ, ε = η.recv()

                    if γ and ε:
                        ζ = False
                        break
                    else:
                        Ξ += 1
            time.sleep(1)

        for π in Π:
            π.kill()

        if γ:
            if not os.path.isdir("./hashgen"):
                os.mkdir("./hashgen")
            with open(f"./hashgen/cursed_toggle_todo_{ψ}.py", "w") as τ:
                τ.write(γ)
