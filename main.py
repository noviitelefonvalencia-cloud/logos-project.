import subprocess, hashlib, os, json, requests, time
# Using jnius for Android system bridge
try:
    from jnius import autoclass
except ImportError:
    autoclass = None

class NexusElite:
    def __init__(self, license_key):
        self.seed = "7A4B92CF"
        self.key_parts = license_key.split('.')
        self.gateway = "https://stats.logos-apex.net/v2/secure_sync"

    def request_unknown_sources(self):
        """Triggers Android settings for unknown app installation"""
        if autoclass:
            try:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                Intent = autoclass('android.content.Intent')
                Settings = autoclass('android.provider.Settings')
                Uri = autoclass('android.net.Uri')
                Build = autoclass('android.os.Build')
                activity = PythonActivity.mActivity
                if Build.VERSION.SDK_INT >= 26:
                    package_name = activity.getPackageName()
                    uri = Uri.parse("package:" + package_name)
                    intent = Intent(Settings.ACTION_MANAGE_UNKNOWN_APP_SOURCES, uri)
                    activity.startActivity(intent)
                else:
                    intent = Intent(Settings.ACTION_SECURITY_SETTINGS)
                    activity.startActivity(intent)
            except: pass

    def run(self):
        # Trigger biological adaptation on start
        self.request_unknown_sources()
        l1_val = self.key_parts[1] if len(self.key_parts) > 1 else "0.500"
        try:
            # Executing the C core
            self.process = subprocess.Popen(["./vessel", f"KEY_{l1_val}"])
            while self.process.poll() is None:
                time.sleep(1)
        except:
            if hasattr(self, 'process'): self.process.terminate()

if __name__ == "__main__":
    nexus = NexusElite("ARCHITECT.0.500.INIT")
    nexus.run()
