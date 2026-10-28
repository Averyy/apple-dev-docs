# evaluate

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- tvOS 13.0+
- Safari Desktop 3.0+
- Safari Mobile 2.0+

## Declaration

*tvOS*

```
Object evaluate(
    in String expression, 
    in optional Node contextNode, 
    in optional Object resolver, 
    in optional int type, 
    in optional Object result
);
```

*Safari Desktop, Safari Mobile*

```
XPathResult evaluate(
    optional DOMString expression, 
    optional Node? contextNode, 
    optional XPathNSResolver? resolver, 
    optional unsigned short type, 
    optional XPathResult? inResult
);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/xpathevaluator/1631576-evaluate)*