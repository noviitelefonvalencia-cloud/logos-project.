import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform
from ctypes import CDLL

class ApexApp(App):
    def prepare_vault(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
            
            # Internal private storage path
            files_path = os.path.dirname(os.path.abspath(__file__))
            vault_path = os.path.join(files_path, '.license_vault')
            
            if not os.path.exists(vault_path):
                os.makedirs(vault_path)
                with open(os.path.join(vault_path, 'presence.log'), 'w') as f:
                    f.write('Resonance waiting...')
        return "Vault Ready"

    def build(self):
        self.prepare_vault()
        status = "Apex Online\n"
        try:
            lib_path = os.path.join(os.getcwd(), "lib", "vessel.so")
            if os.path.exists(lib_path):
                vessel = CDLL(lib_path)
                if vessel.core_main() == 1:
                    status += "Core: Authenticated"
                else:
                    status += "Core: Restricted Mode"
            else:
                status += "Core: Binary Missing"
        except Exception as e:
            status += f"Error: {str(e)}"
        
        return Label(text=status)

if __name__ == '__main__':
    ApexApp().run()
