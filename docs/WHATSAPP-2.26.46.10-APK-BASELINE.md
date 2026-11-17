# WhatsApp 2.26.46.10 — supplied APK baseline

Source: user-supplied file `WhatsApp_V2.26.46.10.apk` (not committed to the repository).

- SHA-256: `9af77e8b62910d14f32a8fdc997ec636afc729a7eedd592810fc3446f41829ba`
- APK archive size: approximately 107 MiB as reported by filesystem listing
- 14 DEX files, 109,544,716 uncompressed DEX bytes
- AndroidManifest.xml: 392,108 bytes (binary Android XML)
- 3 bundled native .so entries

These are archive-level checks, **not** a manifest package/version verification, runtime compatibility test, or validation of obfuscated method signatures. The APK filename is not proof of package metadata. Do not add 2.26.46.10 to the supported version array or enable hooks until manifest identity, DexKit targets, and runtime behavior are verified. Next: use Android SDK APK inspection tools to confirm package/version and compare DexKit method/class matches for each feature, then perform staged device testing.