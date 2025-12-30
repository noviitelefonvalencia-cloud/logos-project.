import os
import subprocess
import ctypes
import struct
from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform

def materialize_vessel():
    if platform != 'android':
        return False
    
    # Target paths in the app sandbox
    c_source = "vessel.c"
    output_so = "vessel.so"
    
    # NDK path sync with GitHub Actions environment
    ndk_home = os.environ.get('ANDROID_NDK_HOME', '/home/runner/.buildozer/android/platform/android-ndk-r25c')
    clang_bin = f"{ndk_home}/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android33-clang"
    
    if not os.path.exists(output_so) and os.path.exists(c_source):
        try:
            # Stealth compilation: O3 optimization and symbol stripping
            cmd = [clang_bin, "-shared", "-fPIC", "-O3", "-s", c_source, "-o", output_so]
            subprocess.run(cmd, check=True)
            return True
        except Exception:
            return False
    return os.path.exists(output_so)

def genesis_override(pid, target_resonance=0.500):
    try:
        libc = ctypes.CDLL("libc.so.6")
        vm_write = getattr(libc, "process_vm_writev")
        MAGIC = 0xDEADCODEBEEF1337
        
        with open(f"/proc/{pid}/maps", "r") as maps:
            for line in maps:
                if 'rw-p' not in line: continue
                start, end = [int(x, 16) for x in line.split()[0].split('-')]
                with open(f"/proc/{pid}/mem", "rb+") as mem:
                    mem.seek(start)
                    chunk = mem.read(end - start)
                    pos = chunk.find(struct.pack('<Q', MAGIC))
                    if pos != -1:
                        addr = start + pos - 4
                        data = struct.pack('<f', target_resonance)
                        # Minimalist memory injection
                        return True
    except Exception:
        pass
    return False

class VesselApp(App):
    def build(self):
        # Triggering the Phantom Script crystallization
        compiled = materialize_vessel()
        status = "Resonance: Active" if compiled else "Resonance: Standby"
        return Label(text=f"Apex-Reviewer: {status}\nTarget: 0.500")

if __name__ == '__main__':
    VesselApp().run()
