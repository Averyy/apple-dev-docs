# gestaltAppleEventsAttr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltAppleEventsAttr = 'evnt'
```

## Discussion

A selector you pass to the `Gestalt` function. If the Apple Event Manager is not present, the `Gestalt` function returns an error value; otherwise, it returns `noErr` and supplies, in the `response` parameter, a 32-bit value whose bits specify which features of the Apple Event Manager are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472598-apple_event_manager_attribute_se/gestaltappleeventsattr)*