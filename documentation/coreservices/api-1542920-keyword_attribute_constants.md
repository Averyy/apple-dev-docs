# Keyword Attribute Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify keyword values for Apple event attributes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum : AEKeyword {
    ...
};
```

## Topics

### Constants
- [keyTransactionIDAttr](./api-1542920-keyword_attribute_constants/keytransactionidattr.md)
  Transaction ID identifying a series of Apple events that are part of one transaction.
- [keyReturnIDAttr](./api-1542920-keyword_attribute_constants/keyreturnidattr.md)
  Return ID for a reply Apple event.
- [keyEventClassAttr](./api-1542920-keyword_attribute_constants/keyeventclassattr.md)
  Event class of an Apple event. See [`AEAddressDesc`](./aeaddressdesc.md).
- [keyEventIDAttr](./api-1542920-keyword_attribute_constants/keyeventidattr.md)
  Event ID of an Apple event. See [`AEAddressDesc`](./aeaddressdesc.md).
- [keyAddressAttr](./api-1542920-keyword_attribute_constants/keyaddressattr.md)
  Address of a target or client application. See also [`AEAddressDesc`](./aeaddressdesc.md).
- [keyOptionalKeywordAttr](./api-1542920-keyword_attribute_constants/keyoptionalkeywordattr.md)
  List of keywords for parameters of an Apple event that should be treated as optional by the target application.
- [keyTimeoutAttr](./api-1542920-keyword_attribute_constants/keytimeoutattr.md)
  Length of time, in ticks, that the client will wait for a reply or a result from the server.
- [keyInteractLevelAttr](./api-1542920-keyword_attribute_constants/keyinteractlevelattr.md)
  Settings for when to allow the Apple Event Manager to bring a server application to the foreground, if necessary, to interact with the user. See [`AEAddressDesc`](./aeaddressdesc.md). (Read-only.)
- [keyEventSourceAttr](./api-1542920-keyword_attribute_constants/keyeventsourceattr.md)
  Nature of the source application. (Read-only.)
- [keyMissedKeywordAttr](./api-1542920-keyword_attribute_constants/keymissedkeywordattr.md)
- [keyOriginalAddressAttr](./api-1542920-keyword_attribute_constants/keyoriginaladdressattr.md)
  Address of original source of Apple event if the event has been forwarded (available only in version 1.01 or later versions of the Apple Event Manager). See also [`AEAddressDesc`](./aeaddressdesc.md).
- [keyReplyRequestedAttr](./api-1542920-keyword_attribute_constants/keyreplyrequestedattr.md)
  A Boolean value indicating whether the Apple event expects to be replied to.
- [keyAcceptTimeoutAttr](./api-1542920-keyword_attribute_constants/keyaccepttimeoutattr.md)
- [keyActualSenderAuditToken](./api-1542920-keyword_attribute_constants/keyactualsenderaudittoken.md)
- [keySenderApplescriptEntitlementsAttr](./api-1542920-keyword_attribute_constants/keysenderapplescriptentitlementsattr.md)
- [keySenderApplicationIdentifierEntitlementAttr](./api-1542920-keyword_attribute_constants/keysenderapplicationidentifierentitlementattr.md)
- [keySenderApplicationSandboxed](./api-1542920-keyword_attribute_constants/keysenderapplicationsandboxed.md)
- [keySenderAuditTokenAttr](./api-1542920-keyword_attribute_constants/keysenderaudittokenattr.md)
- [keySenderEGIDAttr](./api-1542920-keyword_attribute_constants/keysenderegidattr.md)
- [keySenderEUIDAttr](./api-1542920-keyword_attribute_constants/keysendereuidattr.md)
- [keySenderGIDAttr](./api-1542920-keyword_attribute_constants/keysendergidattr.md)
- [keySenderPIDAttr](./api-1542920-keyword_attribute_constants/keysenderpidattr.md)
- [keySenderUIDAttr](./api-1542920-keyword_attribute_constants/keysenderuidattr.md)
- [keyAppleEventAttributesAttr](./api-1542920-keyword_attribute_constants/keyappleeventattributesattr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants)*