import React from 'react'
import ReactDom from 'react-dom'


import Main from "./components/main/main";

import 'antd/dist/antd.less';  // 导入 antd 组件样式
import './assets/css/index.less'; // 用于覆盖上面 antd 定义的变量，必须放在 antd.less 下方

ReactDom.render(<Main />, document.getElementById('root'))