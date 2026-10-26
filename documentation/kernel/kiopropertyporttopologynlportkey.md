# kIOPropertyPortTopologyNLPortKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortTopologyNLPortKey
```

#### Discussion

This key defines the value of NL_Port for the key kIOPropertyPortTopologyKey. If the topology of the port is an NL_Port, this key should be used.

Note: This value can change. It is not a static value.

Requirement: Optional for any interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Topology</key>
   	<string>NL_Port</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyporttopologynlportkey)*