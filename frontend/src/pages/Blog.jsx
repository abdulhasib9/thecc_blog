import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import AppAppBar from '../components/AppAppBar';
import MainContent from '../components/MainContent';
import Latest from '../components/Latest';
import Footer from '../components/Footer';
import AppTheme from '../shared-theme/AppTheme.jsx';
import ImageSlider from "../components/ImageSlider.jsx";
import Custom from '../components/Custom';
import {useEffect, useState} from "react";
import {Category} from "@mui/icons-material";
import CategoryList from "../components/CategoryList.jsx";
import ArticleList from "../components/ArticleList.jsx";
import CopilotInput from "../components/CopilotInput.jsx";
import MainMenu from "../components/MainMenu.jsx";







export default function Blog(props) {


  return (
    <AppTheme {...props}>
      <CssBaseline enableColorScheme />
      <AppAppBar />
      <Container
        maxWidth="lg"
        component="main"
        sx={{ display: 'flex', flexDirection: 'column', my: 16, gap: 4 }}
      >


          <MainMenu />
         
      </Container>
      <Footer />
    </AppTheme>
  );
}
