import os
import random

testing = os.environ.get("SECRET_ENV_FOR_TESTING_ONLY_DO_NOT_USE")

if testing == "1":
    from .cursed_toggle_v1_deprecated import cursed_toggle, _cursed_toggle

elif testing == "2":
    from .cursed_toggle_v2 import cursed_toggle, _cursed_toggle

else:
    if random.randint(1, 2) == 1:
        from .cursed_toggle_v1_deprecated import cursed_toggle, _cursed_toggle

    else:
        from .cursed_toggle_v2 import cursed_toggle, _cursed_toggle