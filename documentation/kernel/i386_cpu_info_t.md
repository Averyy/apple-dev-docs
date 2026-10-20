# i386_cpu_info_t

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.3+

## Declaration

```c
typedef struct i386_cpu_info {
    ...
} i386_cpu_info_t;
```

## Topics

### Instance Properties
- [cache_info](./i386_cpu_info_t/api-1580597-cache_info.md)
- [cache_linesize](./i386_cpu_info_t/api-1580620-cache_linesize.md)
- [cache_partitions](./i386_cpu_info_t/api-1580601-cache_partitions.md)
- [cache_sharing](./i386_cpu_info_t/api-1580518-cache_sharing.md)
- [cache_size](./i386_cpu_info_t/api-1580434-cache_size.md)
- [core_count](./i386_cpu_info_t/api-1580433-core_count.md)
- [cpuid_address_bits_physical](./i386_cpu_info_t/api-1580669-cpuid_address_bits_physical.md)
- [cpuid_address_bits_virtual](./i386_cpu_info_t/api-1580629-cpuid_address_bits_virtual.md)
- [cpuid_arch_perf_leaf](./i386_cpu_info_t/api-1580513-cpuid_arch_perf_leaf.md)
- [cpuid_arch_perf_leafp](./i386_cpu_info_t/api-1580661-cpuid_arch_perf_leafp.md)
- [cpuid_brand](./i386_cpu_info_t/api-1580473-cpuid_brand.md)
- [cpuid_brand_string](./i386_cpu_info_t/api-1580654-cpuid_brand_string.md)
- [cpuid_cache_L2_associativity](./i386_cpu_info_t/api-1580646-cpuid_cache_l2_associativity.md)
- [cpuid_cache_linesize](./i386_cpu_info_t/api-1580492-cpuid_cache_linesize.md)
- [cpuid_cache_size](./i386_cpu_info_t/api-1580575-cpuid_cache_size.md)
- [cpuid_cores_per_package](./i386_cpu_info_t/api-1580480-cpuid_cores_per_package.md)
- [cpuid_cpu_subtype](./i386_cpu_info_t/api-1580502-cpuid_cpu_subtype.md)
- [cpuid_cpu_type](./i386_cpu_info_t/api-1580560-cpuid_cpu_type.md)
- [cpuid_cpufamily](./i386_cpu_info_t/api-1580443-cpuid_cpufamily.md)
- [cpuid_extfamily](./i386_cpu_info_t/api-1580649-cpuid_extfamily.md)
- [cpuid_extfeatures](./i386_cpu_info_t/api-1580653-cpuid_extfeatures.md)
- [cpuid_extmodel](./i386_cpu_info_t/api-1580432-cpuid_extmodel.md)
- [cpuid_family](./i386_cpu_info_t/api-1580511-cpuid_family.md)
- [cpuid_features](./i386_cpu_info_t/api-1580485-cpuid_features.md)
- [cpuid_leaf7_extfeatures](./i386_cpu_info_t/api-3203731-cpuid_leaf7_extfeatures.md)
- [cpuid_leaf7_features](./i386_cpu_info_t/api-1580613-cpuid_leaf7_features.md)
- [cpuid_logical_per_package](./i386_cpu_info_t/api-1580568-cpuid_logical_per_package.md)
- [cpuid_max_basic](./i386_cpu_info_t/api-1580615-cpuid_max_basic.md)
- [cpuid_max_ext](./i386_cpu_info_t/api-1580505-cpuid_max_ext.md)
- [cpuid_microcode_version](./i386_cpu_info_t/api-1580497-cpuid_microcode_version.md)
- [cpuid_model](./i386_cpu_info_t/api-1580570-cpuid_model.md)
- [cpuid_model_string](./i386_cpu_info_t/api-1580666-cpuid_model_string.md)
- [cpuid_mwait_leaf](./i386_cpu_info_t/api-1580525-cpuid_mwait_leaf.md)
- [cpuid_mwait_leafp](./i386_cpu_info_t/api-1580464-cpuid_mwait_leafp.md)
- [cpuid_processor_flag](./i386_cpu_info_t/api-1580422-cpuid_processor_flag.md)
- [cpuid_signature](./i386_cpu_info_t/api-1580660-cpuid_signature.md)
- [cpuid_stepping](./i386_cpu_info_t/api-1580556-cpuid_stepping.md)
- [cpuid_stlb](./i386_cpu_info_t/api-1580579-cpuid_stlb.md)
- [cpuid_thermal_leaf](./i386_cpu_info_t/api-1580637-cpuid_thermal_leaf.md)
- [cpuid_thermal_leafp](./i386_cpu_info_t/api-1580644-cpuid_thermal_leafp.md)
- [cpuid_tlb](./i386_cpu_info_t/api-1580457-cpuid_tlb.md)
- [cpuid_tsc_leaf](./i386_cpu_info_t/api-1580587-cpuid_tsc_leaf.md)
- [cpuid_type](./i386_cpu_info_t/api-1580420-cpuid_type.md)
- [cpuid_vendor](./i386_cpu_info_t/api-1580632-cpuid_vendor.md)
- [cpuid_xsave_leaf](./i386_cpu_info_t/api-1580442-cpuid_xsave_leaf.md)
- [cpuid_xsave_leafp](./i386_cpu_info_t/api-1580445-cpuid_xsave_leafp.md)
- [thread_count](./i386_cpu_info_t/api-1580614-thread_count.md)
- [unused](./i386_cpu_info_t/api-1580507-unused.md)

## See Also

### i386
- [hlt](./api-2870529-hlt.md)
- [inb](./api-1537072-inb.md)
- [do_cpuid](./api-1580421-do_cpuid.md)
- [get_cr0](./api-1571251-get_cr0.md)
- [get_cr2](./api-1571176-get_cr2.md)
- [get_cr3_base](./api-1571286-get_cr3_base.md)
- [get_cr3_raw](./api-1571283-get_cr3_raw.md)
- [get_cr4](./api-1571378-get_cr4.md)
- [get_crc_table](./api-1546895-get_crc_table.md)
- [get_ds](./api-1571328-get_ds.md)
- [get_es](./api-1571424-get_es.md)
- [get_fs](./api-1571293-get_fs.md)
- [get_gs](./api-1571339-get_gs.md)
- [get_ss](./api-1571429-get_ss.md)
- [get_tr](./api-1571379-get_tr.md)
- [cpuid](./api-1580486-cpuid.md)
- [cpuid_cpu_display](./api-1580592-cpuid_cpu_display.md)
- [cpuid_cpufamily](./api-1580564-cpuid_cpufamily.md)
- [cpuid_cpusubtype](./api-1580514-cpuid_cpusubtype.md)
- [cpuid_cputype](./api-1580625-cpuid_cputype.md)
- [cpuid_extfeature_display](./api-1580551-cpuid_extfeature_display.md)
- [cpuid_extfeatures](./api-1580645-cpuid_extfeatures.md)
- [cpuid_family](./api-1580535-cpuid_family.md)
- [cpuid_feature_display](./api-1580655-cpuid_feature_display.md)
- [cpuid_features](./api-1580435-cpuid_features.md)
- [cpuid_get_extfeature_names](./api-1580527-cpuid_get_extfeature_names.md)
- [cpuid_get_feature_names](./api-1580651-cpuid_get_feature_names.md)
- [cpuid_get_leaf7_extfeature_names](./api-3203729-cpuid_get_leaf7_extfeature_names.md)
- [cpuid_get_leaf7_feature_names](./api-1580541-cpuid_get_leaf7_feature_names.md)
- [cpuid_info](./api-1580462-cpuid_info.md)
- [cpuid_leaf7_extfeatures](./api-3203730-cpuid_leaf7_extfeatures.md)
- [cpuid_leaf7_features](./api-1580437-cpuid_leaf7_features.md)
- [cpuid_set_info](./api-1580542-cpuid_set_info.md)
- [clac](./api-1571382-clac.md)
- [clz](./api-1441034-clz.md)
- [clear_ts](./api-1571249-clear_ts.md)
- [cninit](./api-1537074-cninit.md)
- [cpuid_arch_perf_leaf_t](./cpuid_arch_perf_leaf_t.md)
- [cpuid_cache_desc_t](./cpuid_cache_desc_t.md)
- [cpuid_mwait_leaf_t](./cpuid_mwait_leaf_t.md)
- [cpuid_thermal_leaf_t](./cpuid_thermal_leaf_t.md)
- [cpuid_tsc_leaf_t](./cpuid_tsc_leaf_t.md)
- [cpuid_xsave_leaf_t](./cpuid_xsave_leaf_t.md)
- [i386_exception_state_t](./i386_exception_state_t.md)
- [i386_float_state_t](./i386_float_state_t.md)
- [i386_thread_state_t](./i386_thread_state_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/i386_cpu_info_t)*