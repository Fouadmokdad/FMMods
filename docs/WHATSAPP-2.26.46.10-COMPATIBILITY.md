# WhatsApp 2.26.46.10 compatibility audit

## Observed state
- User device reports regular WhatsApp 2.26.46.10 as unsupported.
- Existing FMMods support list covers 2.26.38.xx through 2.26.44.xx.
- The FMMods manager UI and updater-card fix were verified by user screenshot. This does not establish Xposed hook compatibility.

## Source review
- `FeatureLoader.start()` reads the host version and invokes `load()`.
- `load()` initializes DexKit/Unobfuscator and then invokes `checkVersionSupport()` before `initComponents()` and `loadFeatures()`.
- `checkVersionSupport()` compares against the declared version prefixes. Unsupported versions invoke `disableExpirationVersion()`, then throw an exception unless the `bypass_version_check` preference is enabled.
- The preference can therefore allow unsupported host versions to attempt to install hooks. **Do not enable it for testing on a primary WhatsApp installation** without feature-by-feature compatibility validation.
- `loadFeatures()` initializes every registered feature via `FeatureRegistry.features`, so accepting a new version does not mean those hooks are safe.

## Validation gate before declaring support
1. Inspect 2.26.46.10 host structure and method mapping using authorized test environments, with diagnostics and no private user data.
2. Check each feature's unobfuscation lookup and hook target for that host version.
3. Run controlled device tests with a backup/test account, including startup, messaging, media and process restart.
4. Only after successful feature-level testing, update the supported-version list and publish a regular-WhatsApp-only APK.
5. Keep LSPosed module disabled on the user's primary WhatsApp until that validation passes.

No runtime hook compatibility has been demonstrated by this audit.
