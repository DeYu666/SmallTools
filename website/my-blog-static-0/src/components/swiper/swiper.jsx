import React, {Component} from "react";
import { Carousel } from 'antd';


import "./swiper.less"


export default class Swiper extends Component{

    state = {
        posts_data:[
            {
                id:0,
                category:"分类",
                title:"文章标题 1",
            },
            {
                id:2,
                category:"分类",
                title:"文章标题 2",
            },
            {
                id:3,
                category:"分类",
                title:"文章标题 3",
            },
        ]
    }

    render() {
        const {posts_data} = this.state

        return (
            <div>
                <Carousel className={"carousel-container"} autoplay>
                    {posts_data.map((post_data, index)=>(
                        <div className={"flex-column-middle"} key={index}>
                            <div className={"category"}> {post_data.category} </div>
                            <h2> {post_data.title} </h2>
                            <div className={"read-more"}>
                                <a ref={post_data.id}>阅读全文</a>
                            </div>
                        </div>
                    ))}
                </Carousel>
            </div>
        )
    }
}