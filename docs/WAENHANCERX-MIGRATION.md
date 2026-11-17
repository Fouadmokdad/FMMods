# FMMods — WaEnhancerX v2.0.8 migration assessment

Status: source inspection only; no WaEnhancerX source imported and no APK built.

## Source and license
- Upstream: https://github.com/WaEnhancerX/WaEnhancerX (default branch: main)
- Public source license: Apache-2.0; preserve required notices and attribution.
- Original user-provided APK was reported to work on WhatsApp 2.26.46.10; this does not prove compatibility of an independently built fork.

## Verified build blockers (upstream source)
- settings.gradle.kts includes both :app and :licensing.
- app/build.gradle.kts depends on project(":licensing").
- Both debug and release use releaseConfig, which requires a keystore and verifies its certificate fingerprint against the original signing certificate.
- Public repository does not provide the private licensing module and authorized signing material. Do not bypass the licensing module or impersonate the original signing identity.

## Verified Android build parameters
- app namespace: com.waenhancer.app; applicationId: com.waenhancer
- compileSdk 36, targetSdk 36, minSdk 24
- Java/Kotlin toolchain 17; NDK 27.0.12077973; CMake 3.22.1
- VERSION_CODE 20800, VERSION_NAME 2.0.8

## Next safe steps
1. Determine whether maintainers offer an authorized, independently buildable community flavor or access to required private module.
2. If authorized, fork upstream into a separate repository, assign an independent app ID and signing identity, and audit hard-coded package names, Xposed scope, providers, and settings migrations.
3. If not, keep FMMods on its existing independently buildable WaEnhancer base and implement compatible features from documented public interfaces without copying proprietary components.
4. Build CI debug APK, inspect manifest/signature, then test LSPosed injection on WhatsApp 2.26.46.10 before release.

Do not merge into master, publish APKs, or claim device compatibility until verified.
