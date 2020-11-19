import React, {Component} from "react";
import {MailOutlined,EditFilled,TabletFilled} from '@ant-design/icons'
import { Menu } from 'antd';

import "./nav-top.less"

export default class NavTop extends Component{

    state = {
        theme:'',
        navList : [
            {
                path: '/index',
                text: '首页',
                icon: <MailOutlined/>
            },
            {
                path: '/project',
                text: '项目',
                icon: <EditFilled />
            },
            {
                path: '/diary',
                text: '日记',
                icon: <TabletFilled />
            },
        ]
    }

    render() {

        const {navList,theme} = this.state

        return (
            <div>
                <Menu theme={theme} onClick={this.handleClick} mode="horizontal">
                    {
                        navList.map((nav, index) => (
                            <Menu.Item icon={nav.icon} key={nav.path} selected={true}>
                                {nav.text}
                            </Menu.Item>
                        ))
                    }
                </Menu>
            </div>
        )
    }
}