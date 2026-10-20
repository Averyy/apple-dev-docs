# PDEPanel

**Framework**: Application Services  
**Kind**: intf  
**Role**: Protocol

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol PDEPanel
```

```objc
@protocol PDEPanel
```

## Topics

### Instance Methods
- [func panelKind() -> String](./pdepanel/api-3930820-panelkind.md)
- [func panelName() -> String](./pdepanel/api-3930821-panelname.md)
- [func panelView() -> NSView?](./pdepanel/api-3930822-panelview.md)
- [func ppdOptionKeyValueDidChange(String, ppdChoice: String)](./pdepanel/api-3930823-ppdoptionkeyvaluedidchange.md)
- [func printWindowWillClose(Bool)](./pdepanel/api-3930824-printwindowwillclose.md)
- [func restoreValues()](./pdepanel/api-3930825-restorevalues.md)
- [func saveValues()](./pdepanel/api-3930826-savevalues.md)
- [func shouldHide() -> Bool](./pdepanel/api-3930827-shouldhide.md)
- [func shouldPrint() -> Bool](./pdepanel/api-3930828-shouldprint.md)
- [func shouldShowHelp() -> Bool](./pdepanel/api-3930829-shouldshowhelp.md)
- [func summaryInfo() -> [String : String]?](./pdepanel/api-3930830-summaryinfo.md)
- [func supportedPPDOptionKeys() -> [String]?](./pdepanel/api-3930831-supportedppdoptionkeys.md)
- [func willShow()](./pdepanel/api-3930832-willshow.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pdepanel)*