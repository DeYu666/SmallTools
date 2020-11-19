import React, {Component} from "react";


import './user-navs.less'
import UserTitle from "../user-title/user-title";


export default class UserNavs extends Component{

    state = {
        navs:[
            {
                id:'1',
                name:"区块链"
            },
            {
                id:'2',
                name:"Gradle"
            },
        ]
    }

    handleClick = id => {
        console.log(id)
    }

    render() {
        const {navs} = this.state
        return (
            <>
                <UserTitle title={"导航"} />
                <ul className="user_navs">
                    {
                        navs.map((nav, index) => (
                            <li key={index}><a onClick={this.handleClick.bind(this,nav.id)} target="_self">{nav.name}</a></li>
                        ))
                    }
                </ul>
            </>

        )
    }
}

