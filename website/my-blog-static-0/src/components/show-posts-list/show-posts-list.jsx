import React, {Component} from "react";
import {Col, Row} from "antd";

import NavPosts from "../nav-posts/nav-posts";
import Card from "../card/card";   // 导入卡片组件


export default class ShowPostsList extends Component{
    render() {
        return (
            <Row gutter={[32, 24]}>
                <Col span={24}> <NavPosts /> </Col>
                {/* 导入三张文章卡片 */}
                <Col span={6}>
                    <Card />
                </Col>
                <Col span={6}>
                    <Card />
                </Col>
                <Col span={6}>
                    <Card />
                </Col>
            </Row>
        )
    }
}