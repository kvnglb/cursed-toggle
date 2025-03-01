import os
import random

testing = os.environ.get("SECRET_ENV_FOR_TESTING_ONLY_DO_NOT_USE")
r = random.randint(1, 3)

if testing == "1" or (not testing and r == 1):
    from .cursed_toggle_v1_deprecated import cursed_toggle, _cursed_toggle

elif testing == "2" or (not testing and r == 2):
    from .cursed_toggle_v2 import cursed_toggle, _cursed_toggle

elif testing == "3" or (not testing and r == 3):
    from .cursed_toggle_just_a_temp_little_experiment import cursed_toggle, _cursed_toggle
