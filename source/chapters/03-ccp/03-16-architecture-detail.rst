CCP机台整体架构详解
===========

CCP机台整体架构详解
-----------

典型的CCP刻蚀机台由以下子系统组成：

.. mermaid::

   graph TB
       subgraph CCP机台完整架构
           subgraph 工艺模块
               CH[反应腔 Chamber]
               SH[Showerhead]
               ESC[静电吸盘 ESC]
               FR[聚焦环]
           end

           subgraph 气体系统
               GS[气源]
               MFC[MFC]
               GM[混气室]
           end

           subgraph 真空系统
               TV[节流阀]
               TMP[分子泵]
               DP[干泵]
           end

           subgraph RF系统
               HF[高频RF 27-60MHz]
               LF[低频RF 400K-2MHz]
               MN1[匹配网络1]
               MN2[匹配网络2]
           end

           subgraph 温控系统
               TC[ESC加热/冷却]
               HC[He背冷]
               WC[腔体水冷]
           end

           subgraph 控制系统
               PC[工艺控制器]
               EP[Endpoint检测]
           end

           GS --> MFC --> GM --> SH
           SH --> CH
           CH --> TV --> TMP --> DP
           HF --> MN1 --> SH
           LF --> MN2 --> ESC
           TC --> ESC
           HC --> ESC
           WC --> CH
           PC -->|控制所有子系统| CH
       end

       style CH fill:#e1ffe1
       style ESC fill:#ffe1e1
       style HF fill:#e1f5ff
       style LF fill:#ffe1f5

**机台操作流程**：

1. **晶圆装载**：
   - Load Lock抽真空
   - 机械手将晶圆传入腔体
   - 顶针升起接收晶圆
   - 顶针落下，晶圆置于ESC表面
   - He背冷开启，ESC吸附晶圆

2. **工艺准备**：
   - 腔体抽真空至基础压力（<1 mTorr）
   - 调节气压至工艺设定点
   - 开启温控系统
   - ESC温度稳定

3. **刻蚀工艺**：
   - 通入工艺气体
   - 点燃等离子体（RF点火）
   - 调节RF功率至目标值
   - 开始刻蚀
   - Endpoint检测
   - 停止RF，关闭气体

4. **晶圆卸载**：
   - 腔体充N₂至大气压
   - ESC释放晶圆
   - 顶针升起
   - 机械手取出晶圆

5. **腔体清洁**：
   - 定期CF₄/O₂等离子体清洁
   - 去除腔体壁沉积物

**关键工艺参数监控**：

- 气压（Pressure）
- RF功率（RF Power）
- 反射功率（Reflected Power）
- 气体流量（Gas Flow）
- 温度（Temperature）
- He流量（He Flow）
- Vdc（直流偏置电压）
- OES（光学发射光谱）
