# kpc_counterbuf_free

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 11.0+

## Declaration

```c
void kpc_counterbuf_free(uint64_t *);
```

## See Also

### kpc
- [kpc_arch_init](./api-1572346-kpc_arch_init.md)
- [kpc_configurable_config_count](./api-1572369-kpc_configurable_config_count.md)
- [kpc_configurable_count](./api-1572402-kpc_configurable_count.md)
- [kpc_configurable_max](./api-1572351-kpc_configurable_max.md)
- [kpc_controls_counter](./api-1572431-kpc_controls_counter.md)
- [kpc_controls_fixed_counters](./api-1572385-kpc_controls_fixed_counters.md)
- [kpc_counterbuf_alloc](./api-1572340-kpc_counterbuf_alloc.md)
- [kpc_fixed_config_count](./api-1572325-kpc_fixed_config_count.md)
- [kpc_fixed_count](./api-1572322-kpc_fixed_count.md)
- [kpc_fixed_max](./api-1572415-kpc_fixed_max.md)
- [kpc_force_all_ctrs](./api-1572429-kpc_force_all_ctrs.md)
- [kpc_force_all_ctrs_arch](./api-1572433-kpc_force_all_ctrs_arch.md)
- [kpc_get_actionid](./api-1572427-kpc_get_actionid.md)
- [kpc_get_all_cpus_counters](./api-1572398-kpc_get_all_cpus_counters.md)
- [kpc_get_classes](./api-1572364-kpc_get_classes.md)
- [kpc_get_config](./api-1572417-kpc_get_config.md)
- [kpc_get_config_count](./api-1572387-kpc_get_config_count.md)
- [kpc_get_configurable_config](./api-1572423-kpc_get_configurable_config.md)
- [kpc_get_configurable_counters](./api-1572334-kpc_get_configurable_counters.md)
- [kpc_get_configurable_pmc_mask](./api-1572341-kpc_get_configurable_pmc_mask.md)
- [kpc_get_counter_count](./api-1572416-kpc_get_counter_count.md)
- [kpc_get_counterbuf_size](./api-3037458-kpc_get_counterbuf_size.md)
- [kpc_get_cpu_counters](./api-1572419-kpc_get_cpu_counters.md)
- [kpc_get_curcpu_counters](./api-1572335-kpc_get_curcpu_counters.md)
- [kpc_get_curthread_counters](./api-1572391-kpc_get_curthread_counters.md)
- [kpc_get_fixed_config](./api-1572376-kpc_get_fixed_config.md)
- [kpc_get_fixed_counters](./api-1572343-kpc_get_fixed_counters.md)
- [kpc_get_force_all_ctrs](./api-1572336-kpc_get_force_all_ctrs.md)
- [kpc_get_period](./api-1572422-kpc_get_period.md)
- [kpc_get_pmu_version](./api-1572386-kpc_get_pmu_version.md)
- [kpc_get_rawpmu_config](./api-1572412-kpc_get_rawpmu_config.md)
- [kpc_get_running](./api-1572420-kpc_get_running.md)
- [kpc_get_shadow_counters](./api-1572328-kpc_get_shadow_counters.md)
- [kpc_get_thread_counting](./api-1572344-kpc_get_thread_counting.md)
- [kpc_idle](./api-1572405-kpc_idle.md)
- [kpc_idle_exit](./api-1572370-kpc_idle_exit.md)
- [kpc_init](./api-1572384-kpc_init.md)
- [kpc_is_running_configurable](./api-1572390-kpc_is_running_configurable.md)
- [kpc_is_running_fixed](./api-1572434-kpc_is_running_fixed.md)
- [kpc_multiple_clients](./api-1572342-kpc_multiple_clients.md)
- [kpc_pm_acknowledge](./api-2870519-kpc_pm_acknowledge.md)
- [kpc_popcount](./api-1572350-kpc_popcount.md)
- [kpc_rawpmu_config_count](./api-1572404-kpc_rawpmu_config_count.md)
- [kpc_register_cpu](./api-1572424-kpc_register_cpu.md)
- [kpc_register_pm_handler](./api-1572430-kpc_register_pm_handler.md)
- [kpc_release_pm_counters](./api-1572327-kpc_release_pm_counters.md)
- [kpc_reserve_pm_counters](./api-1572395-kpc_reserve_pm_counters.md)
- [kpc_sample_kperf](./api-1572393-kpc_sample_kperf.md)
- [kpc_set_actionid](./api-1572379-kpc_set_actionid.md)
- [kpc_set_config](./api-1572437-kpc_set_config.md)
- [kpc_set_config_arch](./api-1572396-kpc_set_config_arch.md)
- [kpc_set_period](./api-1572418-kpc_set_period.md)
- [kpc_set_period_arch](./api-1572380-kpc_set_period_arch.md)
- [kpc_set_running](./api-1572411-kpc_set_running.md)
- [kpc_set_running_arch](./api-1572368-kpc_set_running_arch.md)
- [kpc_set_sw_inc](./api-1572355-kpc_set_sw_inc.md)
- [kpc_set_thread_counting](./api-1572378-kpc_set_thread_counting.md)
- [kpc_thread_ast_handler](./api-1572357-kpc_thread_ast_handler.md)
- [kpc_thread_create](./api-1572348-kpc_thread_create.md)
- [kpc_thread_destroy](./api-1572383-kpc_thread_destroy.md)
- [kpc_unregister_cpu](./api-1645398-kpc_unregister_cpu.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1572361-kpc_counterbuf_free)*