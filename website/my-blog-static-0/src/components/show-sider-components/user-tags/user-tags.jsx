import React, {Component} from "react";

import './user-tags.less'
import UserTitle from "../user-title/user-title";


export default class UserTags extends Component{

    state = {
        tags:[
            {
                id:'1',
                name:"git"
            },
            {
                id:'2',
                name:"markdown"
            },
        ]
    }

    handleClick = id => {
        console.log(id)
    }


    render() {
        const {tags} = this.state
        return (
            <>
                <UserTitle title={"标签"} />
                <ul className="user_tags">
                    {
                        tags.map((tag, index) => (
                            <li key={index}><a target="_self" onClick={this.handleClick.bind(this,tag.id)}>{tag.name}</a></li>
                        ))
                    }
                </ul>
            </>
        )
    }
}