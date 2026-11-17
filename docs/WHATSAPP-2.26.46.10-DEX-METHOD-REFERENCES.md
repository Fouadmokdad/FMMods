# WhatsApp 2.26.46.10 — DEX method-reference evidence

Examined the **actual user-supplied APK** (not a similarly named release) with a DEX parser. Parsed string IDs, class_data encoded methods, code_item instruction arrays, and `const-string` (opcode 0x1a) references. The method IDs below are **DEX-local IDs**, not cross-version stable descriptors. A byte-level instruction scan can produce false positives; confirm with a full instruction decoder / DexKit before enabling hooks.

| FMMods query anchor | DEX | Methods containing a const-string reference |
| --- | --- | --- |
| `presencestatemanager/setAvailable/new-state` | classes.dex | 1 (method ID 21001) |
| `ReadReceiptUtils/buildReadReceiptHandler malformed` | classes.dex | 1 (23721) |
| `chatInfo/incrementUnseenImportantMessageCount` | classes.dex | 1 (23407) |
| `FMessage/getSenderUserJid/key.id` | classes.dex | 1 (27242) |
| `UserActionsMessageForwarding/userActionForwardMessage` | classes7.dex | 1 (5527) |
| `HandleMeComposing/sendComposing` | classes9.dex | 1 (8894) |
| `SharedMessageProcessor/handlePlaintext` | classes9.dex | **2 (23788, 29524)** |

**Compatibility implications:** The forwarding fallback anchor has an identifiable candidate. The plaintext handler anchor has **two** candidate methods; FMMods' `findFirstMethodUsingStrings` currently selects the first method without checking a signature, so this query needs a method-signature disambiguation check before declaring support.

These checks are more specific than string presence but still do **not** validate method signatures, class-loader resolution, feature behavior, or device stability. Keep 2.26.46.10 excluded from supported versions pending those gates.
