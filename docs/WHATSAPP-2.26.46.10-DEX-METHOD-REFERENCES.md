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

## Decoded method_id signatures from the supplied APK

Decoded DEX `method_ids`, `proto_ids`, and `type_list` directly (no signature inferred from anchor text):

- `classes9.dex` method 23788: `LX/GnH;->A00(LX/HfU;LX/G5B;LX/1jo;LX/1jo;LX/G7F;Ljava/lang/Integer;[BZZZ)V` — void, contains byte array.
- `classes9.dex` method 29524: `LX/HCQ;->A03(LX/HfU;LX/G5B;LX/1jo;LX/Fpk;LX/HCQ;)Z` — boolean, no byte array.
- `classes7.dex` forwarding candidate method 5527: `LX/AiB;->A00(LX/BrM;LX/AiB;LX/19H;LX/CIg;LX/Bob;Ljava/util/List;Z)LX/BzC;`.

The signature-based plaintext filter introduced in commit `e5f35fd` therefore discriminates the two observed methods on this APK. These are obfuscated, version-specific identifiers, not stable cross-version API names. Runtime hook behavior remains unverified.
