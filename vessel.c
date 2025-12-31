#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Resonance signature: 0x88f2
int core_main() {
    // Dynamic path discovery for Android environment
    const char *vault_path = ".license_vault/key.pub";
    FILE *file = fopen(vault_path, "r");
    
    if (file == NULL) {
        // Fallback for absolute internal path
        file = fopen("/data/user/0/org.vessel.ether/files/.license_vault/key.pub", "r");
    }

    if (file != NULL) {
        char buffer[10];
        if (fgets(buffer, sizeof(buffer), file) != NULL) {
            // Checking for the 0x88f2 signature
            if (strstr(buffer, "88f2") != NULL) {
                fclose(file);
                return 1; // RESONANCE_ACTIVE
            }
        }
        fclose(file);
    }
    return 0; // CORE_LOCKED
}
