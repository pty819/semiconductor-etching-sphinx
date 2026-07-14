CCP机台整体架构详解
===================

典型的CCP刻蚀机台由多个子系统协同工作，每个子系统都有其特定的功能和设计考量。

系统架构总览
-----------

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

机台操作流程
-----------

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

关键工艺参数监控
---------------

CCP机台在工艺过程中需要实时监测的关键参数包括：

.. list-table:: 关键工艺参数及其作用
   :header-rows: 1
   :widths: 25 25 50

   * - 参数
     - 典型范围
     - 监控目的
   * - 气压（Pressure）
     - 5-200 mTorr
     - 控制等离子体密度和离子能量分布
   * - RF功率（RF Power）
     - 100-2000W
     - 控制等离子体密度和刻蚀速率
   * - 反射功率（Reflected Power）
     - <5%正向功率
     - 确保阻抗匹配，防止设备损坏
   * - 气体流量（Gas Flow）
     - 10-500 sccm
     - 控制反应物浓度和刻蚀化学
   * - 温度（Temperature）
     - -20~400°C
     - 控制刻蚀选择性和侧壁形貌
   * - He流量（He Flow）
     - 1-10 sccm
     - 确保晶圆与ESC的热接触
   * - Vdc（直流偏置电压）
     - -50~-500V
     - 直接反映离子轰击能量
   * - OES（光学发射光谱）
     - 多波长监测
     - Endpoint检测和等离子体状态监控

子系统间协同
------------

CCP机台的各子系统需要精密协同才能保证工艺的稳定性和可重复性：

**气体系统与真空系统的平衡**
* MFC控制进气量，节流阀控制排气量
* 两者协同决定腔体气压的稳定
* 典型稳定时间：3-5秒达到目标气压

**RF系统与温控系统的配合**
* RF功率直接影响晶圆温度
* 温控系统需要实时调整He流量和ESC温度
* 典型温度稳定时间：<30秒

**Endpoint检测与工艺控制的闭环**
* OES实时监测刻蚀产物
* 检测到终点信号后自动停止刻蚀
* 过刻蚀（Over-etch）时间可精确控制
