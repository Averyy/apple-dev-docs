# kIOPropertyPortTopologyAutomaticKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- DriverKit 20.0+
- macOS 10.3+

## Declaration

```c
#define kIOPropertyPortTopologyAutomaticKey
```

## Discussion

This key defines the value of Automatic for the key kIOPropertyPortTopologyKey. If the topology of the port is automatically adjusted by the host/device and a definitive topology is not known, this key should be used.

Note: This value can change. It is not a static value.

Requirement: Optional for any interconnect.

Example:

```occ
 
 
<dict>
   <key>Controller Characteristics</key>
   <dict>
   	<key>Port Topology</key>
   	<string>Automatic</string>
   </dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiopropertyporttopologyautomatickey)*