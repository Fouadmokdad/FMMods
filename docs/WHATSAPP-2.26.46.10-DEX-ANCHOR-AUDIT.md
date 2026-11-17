# WhatsApp 2.26.46.10 — actual DEX string-anchor audit

Inspected the user-supplied `WhatsApp_V2.26.46.10.apk` directly. Parsed the DEX string_id tables in all `classes*.dex` entries and searched for exact string fragments referenced by FMMods `Unobfuscator.kt`. This is a **static anchor-presence** check, not DexKit method-resolution or runtime validation.

| Anchor used by FMMods | DEX result |
| --- | --- |
| `presencestatemanager/setAvailable/new-state` | classes.dex |
| `HandleMeComposing/sendComposing` | classes9.dex |
| `SharedMessageProcessor/handlePlaintext` | classes9.dex |
| `ProtocolTreeNode/getAttributeJid` | classes.dex |
| `ReadReceiptUtils/buildReadReceiptHandler malformed` | classes.dex |
| `chatInfo/incrementUnseenImportantMessageCount` | classes.dex |
| `UPDATE_MESSAGE_MAIN_BROADCAST_SCAN_SQL` | classes.dex |
| `UserActions/userActionForwardMessage` | **NOT FOUND** |
| `UserActionsMessageForwarding/userActionForwardMessage` | classes7.dex |
| `FMessage/getSenderUserJid/key.id` | classes.dex |
| `No HomeFragment mapping for community tab id:` | classes.dex |
| `SendReadReceiptJob` | classes.dex, classes9.dex |

**11/12 anchors present**, including the alternative forwarding anchor already specified by the `anyOf` query in `loadForwardClassMethod`. No source modification is justified solely by this missing legacy string.

## Next verification gates

1. Run actual DexKit queries against this exact APK and record match counts and method descriptors; confirm expected parameter and return types.
2. Investigate queries based on opcodes, field types, numbers, and invoked methods; they cannot be validated by string presence.
3. Run isolated, opt-in device testing with per-feature logs and rollback. Do not mark this version supported or enable all hooks on a primary WhatsApp installation based on static results.
