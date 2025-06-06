# passThruParams

**Framework**: Core Services  
**Kind**: structp

A pointer to an Apple event descriptor that ispassed untouched as an optional parameter, with keyword `keyAEPropData` (`'prdt'`),in the Apple event sent to each application launched or activated(whether individual preferred applications or the application designatedby `appRef`). See the  in the Carbon Interapplication CommunicationDocumentation for a description of the `AEDesc` datatype. The value of this field can be `NULL`.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

## Declaration

```swift
var passThruParams: UnsafePointer<AEDesc>!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1445933-passthruparams)*