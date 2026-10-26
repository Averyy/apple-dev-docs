# keyMissedKeywordAttr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
keyMissedKeywordAttr = 'miss'
```

#### Discussion

Keyword for first required parameter remaining in an Apple event. (Read only.)

After extracting all known Apple event parameters from an event, your handler should check whether the `keyMissedKeywordAttr` attribute exists. If so, your handler has not retrieved all the parameters that the source application considered to be required, and it should return an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1542920-keyword_attribute_constants/keymissedkeywordattr)*