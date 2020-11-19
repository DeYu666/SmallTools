import React, {Component} from "react";
import {Layout} from 'antd'


import NavTop from "../nav-top/nav-top";
import Show from "../show/show";
import FooterMy from "../footer/footer";
import PostDetail from "../post-detail/post-detail";
import Tags from "../tags/tags";



const { Header, Footer, Content } = Layout;

export default class Main extends Component{
    render() {
        return (
            <Layout>
                <Header>
                    <NavTop />
                </Header>

                <Content style={{ padding: '0 50px', marginTop: 10 }}>
                    <Show />
                    {/*<PostDetail />*/}
                    {/*<Tags />*/}
                </Content>

                <Footer>
                    <FooterMy />
                </Footer>
            </Layout>
        )
    }
}