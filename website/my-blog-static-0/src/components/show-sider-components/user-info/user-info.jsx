import React, {Component} from "react";
import {Avatar} from "antd";

import './user-info.less'
import head_img from "./img/head_img.jpg";


export default class UserInfo extends Component{

    state = {
        icon:head_img,
        nickname: "Asa",
        description:"独属于我自己的个人小站",
    }

    render() {
        const {icon, nickname, description} = this.state
        return (
            <div className="user_info" style={{"marginTop": 10, "display": "flex"}}>
                <Avatar className="authorImg" shape="square" size={64} src={icon}  style={{"float":'left'}} />
                <div className="meta" style={{"float":'left'}}>
                    <div className="name">
                        {nickname}
                    </div>
                    <div className="description">
                        {description}
                    </div>
                </div>
            </div>
        )
    }
}