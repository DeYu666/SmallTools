import React, {Component} from "react";

import "./switch.less"
import {AliwangwangFilled, ApiFilled} from  '@ant-design/icons';
import PropTypes from "prop-types";

export default class Switch extends Component{

    static propTypes = {
        handleSwitch: PropTypes.func
    }

    state = {
        is_first : true,
        one_img:  <AliwangwangFilled style={{fontSize:23}} />,
        two_img: <ApiFilled style={{fontSize:23}} />,
    }

    handleChange = (location) => {
        if(location === "first"){
            this.setState({is_first:true})
            this.props.handleSwitch(true)
        }
        else{
            this.setState({is_first :false})
            this.props.handleSwitch(false)
        }
    }

    render() {
        const {is_first,one_img,two_img} = this.state
        return (
            <div className="sidebarMenu">
                <ul className="menu">
                    <li className="anchor-my" style={is_first ? {"left":1} : {"left":39}} />
                    <li className={is_first ? "active" : null} >
                        <a onClick={this.handleChange.bind(this, "first")}>
                            {one_img}
                        </a>
                    </li>
                    <li className={is_first ? null : "active"}>
                        <a onClick={this.handleChange.bind(this,"second")}>
                            {two_img}
                        </a>
                    </li>
                </ul>
            </div>
        )
    }
}