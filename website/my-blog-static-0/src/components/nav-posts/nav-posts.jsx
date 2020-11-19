import React, {Component} from "react";

import "./nav-posts.less"

export default class NavPosts extends Component{

    state = {
        current: 3,
        sub_current: -1,
        categories_data:[
            {
                id: 3,
                name:"最新撰写"
            },
            {
                id: 7,
                name:"编程语言",
                cub_cate:[
                    {
                        name:"gradle",
                        id: 3,
                    },
                    {
                        name:"React",
                        id: 7,
                    }
                ]

            }
        ]
    }

    handleClick = (id, sub_id) => {
        console.log(id)
        this.setState({ current: id,sub_current: sub_id });
    };

    render() {

        const {categories_data,current,sub_current} = this.state

        return (
            <div className={"categoryNav"}>
                {
                    categories_data.map((category,index) => (
                        <div className={`dropdown ${current === category.id ? 'active' : null }`}
                             onClick={category.cub_cate === undefined && current !== category.id ? this.handleClick.bind(this,category.id) : null }
                             style={{marginLeft:0}} key={index} >
                            <span>{category.name}</span>
                            { category.cub_cate === undefined ? null : (
                                <div className={"dropdown-content"}>
                                    { category.cub_cate.map((cate, index) => (
                                        <p className={sub_current === cate.id ? 'active' : null }
                                           onClick={sub_current !== cate.id ? this.handleClick.bind(this, category.id, cate.id):null}
                                           key={index} >{cate.name}</p>
                                    ) ) }
                                </div>
                            ) }
                        </div>
                    ))
                }
            </div>
        )
    }
}