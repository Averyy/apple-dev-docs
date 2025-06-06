# Keyword Attribute Constants

**Framework**: Core Services

Specify keyword values for Apple event attributes.

#### Overview

These constants are keyword constants for Apple event attributes. An Apple event consists of attributes (which identify the Apple event and denote its task) and, often, parameters (which contain information to be used by the target application). An Apple event attribute is a descriptor that identifies the event class, event ID, target application, or some other characteristic of the Apple event. Taken together, the attributes of an Apple event denote the task to be performed on any data specified in the Apple event’s parameters.

Keywords are arbitrary names used by the Apple Event Manager to keep track of various descriptors. Your application cannot examine the contents of an Apple event directly. Instead, you call Apple Event Manager routines such as those described in [`Getting Data or Descriptors From Apple Events and Apple Event Records`](https://developer.apple.com/documentation/applicationservices/apple_event_manager#1651986) to request attributes and parameters by keyword.

See also [`Keyword Parameter Constants`](apple_events/1527206-keyword_parameter_constants.md).

##### 1770283

The constant `keyReplyRequestedAttr` was added in OS X version 10.3.

## Topics

### Constants
- [var keyTransactionIDAttr: AEKeyword](keytransactionidattr.md)
  Transaction ID identifying a series of Apple events that are part of one transaction.
- [var keyReturnIDAttr: AEKeyword](keyreturnidattr.md)
  Return ID for a reply Apple event.
- [var keyEventClassAttr: AEKeyword](keyeventclassattr.md)
  Event class of an Apple event. See [`AEAddressDesc`](aeaddressdesc.md).
- [var keyEventIDAttr: AEKeyword](keyeventidattr.md)
  Event ID of an Apple event. See [`AEAddressDesc`](aeaddressdesc.md).
- [var keyAddressAttr: AEKeyword](keyaddressattr.md)
  Address of a target or client application. See also [`AEAddressDesc`](aeaddressdesc.md).
- [var keyOptionalKeywordAttr: AEKeyword](keyoptionalkeywordattr.md)
  List of keywords for parameters of an Apple event that should be treated as optional by the target application.
- [var keyTimeoutAttr: AEKeyword](keytimeoutattr.md)
  Length of time, in ticks, that the client will wait for a reply or a result from the server.
- [var keyInteractLevelAttr: AEKeyword](keyinteractlevelattr.md)
  Settings for when to allow the Apple Event Manager to bring a server application to the foreground, if necessary, to interact with the user. See [`AEAddressDesc`](aeaddressdesc.md). (Read-only.)
- [var keyEventSourceAttr: AEKeyword](keyeventsourceattr.md)
  Nature of the source application. (Read-only.)
- [var keyMissedKeywordAttr: AEKeyword](keymissedkeywordattr.md)
- [var keyOriginalAddressAttr: AEKeyword](keyoriginaladdressattr.md)
  Address of original source of Apple event if the event has been forwarded (available only in version 1.01 or later versions of the Apple Event Manager). See also [`AEAddressDesc`](aeaddressdesc.md).
- [var keyReplyRequestedAttr: AEKeyword](keyreplyrequestedattr.md)
  A Boolean value indicating whether the Apple event expects to be replied to.
- [var keyAcceptTimeoutAttr: AEKeyword](keyaccepttimeoutattr.md)
- [var keyActualSenderAuditToken: AEKeyword](keyactualsenderaudittoken.md)
- [var keySenderApplescriptEntitlementsAttr: AEKeyword](keysenderapplescriptentitlementsattr.md)
- [var keySenderApplicationIdentifierEntitlementAttr: AEKeyword](keysenderapplicationidentifierentitlementattr.md)
- [var keySenderApplicationSandboxed: AEKeyword](keysenderapplicationsandboxed.md)
- [var keySenderAuditTokenAttr: AEKeyword](keysenderaudittokenattr.md)
- [var keySenderEGIDAttr: AEKeyword](keysenderegidattr.md)
- [var keySenderEUIDAttr: AEKeyword](keysendereuidattr.md)
- [var keySenderGIDAttr: AEKeyword](keysendergidattr.md)
- [var keySenderPIDAttr: AEKeyword](keysenderpidattr.md)
- [var keySenderUIDAttr: AEKeyword](keysenderuidattr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1542920-keyword_attribute_constants)*