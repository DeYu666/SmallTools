import React, {Component} from "react";

import "./card.less"

export default class Card extends Component{

    state = {
        img_src:"https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=4166449390,244951508&fm=26&gp=0.jpg",
        title:"",
        abstract:"文章摘要。。。。",
        create_time:"2020年1月30日",
        category:"gradle",
        tags:[{
            id:0,
            name:"标签-1",
        },{
            id:2,
            name:"标签 - 2",
        },],
    }


    render() {
        const {img_src,tags,title,abstract,category,create_time} = this.state
        return (
            <div className={"card"}>
                <a>
                    <div className={"card-image"}>
                        <img src={img_src} />
                        <span className={"card-title"}>{title}</span>
                        <span className={"posts-date"}>
                            {create_time}&nbsp;&nbsp;·&nbsp;&nbsp;{category}
                        </span>
                    </div>
                </a>
                <div className={"card-content  article-content"}>
                    <div className={"summary"}>
                        {abstract}
                    </div>
                </div>
                <div className={"card-action article-tags"}>
                    {tags.map((tag,index) => (
                        <a key={index}> <span className={"chip tag-color"}> {tag.name} </span> </a>
                    ))}
                </div>
            </div>
        )
    }
}