import os
from anticaptchaofficial.turnstileproxyless import *


class AntiCaptcha:
    def find_token(self, url, cookie, site_key):
        solver = turnstileProxyless()
        solver.set_verbose(0)
        solver.set_key(self.get_anticaptcha_api_key())
        solver.set_website_url(url)
        solver.set_cookies("PHPSESSID=" + cookie)
        solver.set_website_key(site_key)

        solver.set_soft_id(0)

        token = solver.solve_and_return_solution()
        if token != 0:
            return token
        else:
            print("task finished with error " + solver.error_code)
            return

    def get_anticaptcha_api_key(self):
        return os.environ['ANTICAPTCHA_API_KEY']