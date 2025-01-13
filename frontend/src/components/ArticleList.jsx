import axios from "axios";


import PropTypes from 'prop-types';
import Avatar from '@mui/material/Avatar';
import AvatarGroup from '@mui/material/AvatarGroup';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid2';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import FormControl from '@mui/material/FormControl';
import InputAdornment from '@mui/material/InputAdornment';
import OutlinedInput from '@mui/material/OutlinedInput';
import { styled } from '@mui/material/styles';
import SearchRoundedIcon from '@mui/icons-material/SearchRounded';
import RssFeedRoundedIcon from '@mui/icons-material/RssFeedRounded';
import {useEffect, useState} from "react";
import Button from '@mui/material/Button';

const PostList = () => {
    const [posts, setPosts] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/blog/api/posts/')
            .then(response => {
                setPosts(response.data);
            })
            .catch(error => {
                setError('There was an error fetching the posts!');
                console.error(error);
            });
    }, []);




    const SyledCard = styled(Card)(({ theme }) => ({
        display: 'flex',
        flexDirection: 'column',
        padding: 0,
        height: '100%',
        backgroundColor: (theme.vars || theme).palette.background.paper,
        '&:hover': {
            backgroundColor: 'transparent',
            cursor: 'pointer',
        },
        '&:focus-visible': {
            outline: '3px solid',
            outlineColor: 'hsla(210, 98%, 48%, 0.5)',
            outlineOffset: '2px',
        },
    }));

    const SyledCardContent = styled(CardContent)({
        display: 'flex',
        flexDirection: 'column',
        gap: 4,
        padding: 16,
        flexGrow: 1,
        '&:last-child': {
            paddingBottom: 16,
        },
    });

    const StyledTypography = styled(Typography)({
        display: '-webkit-box',
        WebkitBoxOrient: 'vertical',
        WebkitLineClamp: 2,
        overflow: 'hidden',
        textOverflow: 'ellipsis',
    });





    return (
        <div>
            {error && <p>{error}</p>}
            <h1>Blog Posts</h1>
            <div className="post-list">
                {posts.map(post => (
                    <div className="post-card" key={post.id}>
                        <h2>{post.title}</h2>
                        {post.main_image && <img src={post.main_image} alt={post.title} />}
                        <p>{post.content.slice(0, 150)}...</p>
                        <a href={`/posts/${post.slug}`}>Read More</a>
                    </div>
                ))}
            </div>




            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 4 }}>




                <Grid container spacing={2} columns={12}>

                    {posts.map(article => (
                        <>
                            <Grid size={{ xs: 12, md: 6 }}>
                                <SyledCard
                                    variant="outlined"
                                    onFocus={() => handleFocus(0)}
                                    onBlur={handleBlur}
                                    tabIndex={0}
                                    className={focusedCardIndex === 0 ? 'Mui-focused' : ''}
                                >
                                    <CardMedia
                                        component="img"
                                        alt="green iguana"
                                        image={cardData[0].img}
                                        sx={{
                                            aspectRatio: '16 / 9',
                                            borderBottom: '1px solid',
                                            borderColor: 'divider',
                                        }}
                                    />
                                    <SyledCardContent>
                                        <Typography gutterBottom variant="caption" component="div">
                                            {article.category.name}
                                        </Typography>
                                        <Typography gutterBottom variant="h6" component="div">
                                            {article.title}
                                        </Typography>
                                        <StyledTypography variant="body2" color="text.secondary" gutterBottom>
                                            {cardData[0].description}
                                        </StyledTypography>
                                    </SyledCardContent>
                                    <Author authors={cardData[0].authors} />
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            justifyContent: 'center',
                                            padding: '16px',
                                            borderTop: '1px solid',
                                            borderColor: 'divider',
                                        }}
                                    >
                                        <Button
                                            variant="contained"
                                            color="primary"
                                            size="small"
                                            sx={{
                                                textTransform: 'capitalize',
                                                fontWeight: 'bold',
                                                borderRadius: 0, // Square edges
                                            }}
                                            onClick={() => console.log('Read More clicked')}
                                        >
                                            Read More
                                        </Button>
                                    </Box>
                                </SyledCard>
                            </Grid>

                        </>
                    ))}









                    <Grid size={{ xs: 12, md: 6 }}>
                        <SyledCard
                            variant="outlined"
                            onFocus={() => handleFocus(0)}
                            onBlur={handleBlur}
                            tabIndex={0}
                            className={focusedCardIndex === 0 ? 'Mui-focused' : ''}
                        >
                            <CardMedia
                                component="img"
                                alt="green iguana"
                                image={cardData[0].img}
                                sx={{
                                    aspectRatio: '16 / 9',
                                    borderBottom: '1px solid',
                                    borderColor: 'divider',
                                }}
                            />
                            <SyledCardContent>
                                <Typography gutterBottom variant="caption" component="div">
                                    {cardData[0].tag}
                                </Typography>
                                <Typography gutterBottom variant="h6" component="div">
                                    {cardData[0].title}
                                </Typography>
                                <StyledTypography variant="body2" color="text.secondary" gutterBottom>
                                    {cardData[0].description}
                                </StyledTypography>
                            </SyledCardContent>
                            <Author authors={cardData[0].authors} />
                        </SyledCard>
                    </Grid>
                    <Grid size={{ xs: 12, md: 6 }}>
                        <SyledCard
                            variant="outlined"
                            onFocus={() => handleFocus(1)}
                            onBlur={handleBlur}
                            tabIndex={0}
                            className={focusedCardIndex === 1 ? 'Mui-focused' : ''}
                        >
                            <CardMedia
                                component="img"
                                alt="green iguana"
                                image={cardData[1].img}
                                aspect-ratio="16 / 9"
                                sx={{
                                    borderBottom: '1px solid',
                                    borderColor: 'divider',
                                }}
                            />
                            <SyledCardContent>
                                <Typography gutterBottom variant="caption" component="div">
                                    {cardData[1].tag}
                                </Typography>
                                <Typography gutterBottom variant="h6" component="div">
                                    {cardData[1].title}
                                </Typography>
                                <StyledTypography variant="body2" color="text.secondary" gutterBottom>
                                    {cardData[1].description}
                                </StyledTypography>
                            </SyledCardContent>
                            <Author authors={cardData[1].authors} />
                        </SyledCard>
                    </Grid>
                    {/*<Grid size={{ xs: 12, md: 4 }}>*/}
                    {/*  <SyledCard*/}
                    {/*    variant="outlined"*/}
                    {/*    onFocus={() => handleFocus(2)}*/}
                    {/*    onBlur={handleBlur}*/}
                    {/*    tabIndex={0}*/}
                    {/*    className={focusedCardIndex === 2 ? 'Mui-focused' : ''}*/}
                    {/*    sx={{ height: '100%' }}*/}
                    {/*  >*/}
                    {/*    <CardMedia*/}
                    {/*      component="img"*/}
                    {/*      alt="green iguana"*/}
                    {/*      image={cardData[2].img}*/}
                    {/*      sx={{*/}
                    {/*        height: { sm: 'auto', md: '50%' },*/}
                    {/*        aspectRatio: { sm: '16 / 9', md: '' },*/}
                    {/*      }}*/}
                    {/*    />*/}
                    {/*    <SyledCardContent>*/}
                    {/*      <Typography gutterBottom variant="caption" component="div">*/}
                    {/*        {cardData[2].tag}*/}
                    {/*      </Typography>*/}
                    {/*      <Typography gutterBottom variant="h6" component="div">*/}
                    {/*        {cardData[2].title}*/}
                    {/*      </Typography>*/}
                    {/*      <StyledTypography variant="body2" color="text.secondary" gutterBottom>*/}
                    {/*        {cardData[2].description}*/}
                    {/*      </StyledTypography>*/}
                    {/*    </SyledCardContent>*/}
                    {/*    <Author authors={cardData[2].authors} />*/}
                    {/*  </SyledCard>*/}
                    {/*</Grid>*/}
                    <Grid size={{ xs: 12, md: 4 }}>
                        <Box
                            sx={{ display: 'flex', flexDirection: 'column', gap: 2, height: '100%' }}
                        >
                            <SyledCard
                                variant="outlined"
                                onFocus={() => handleFocus(3)}
                                onBlur={handleBlur}
                                tabIndex={0}
                                className={focusedCardIndex === 3 ? 'Mui-focused' : ''}
                                sx={{ height: '100%' }}
                            >
                                <SyledCardContent
                                    sx={{
                                        display: 'flex',
                                        flexDirection: 'column',
                                        justifyContent: 'space-between',
                                        height: '100%',
                                    }}
                                >
                                    <div>
                                        <Typography gutterBottom variant="caption" component="div">
                                            {cardData[3].tag}
                                        </Typography>
                                        <Typography gutterBottom variant="h6" component="div">
                                            {cardData[3].title}
                                        </Typography>
                                        <StyledTypography
                                            variant="body2"
                                            color="text.secondary"
                                            gutterBottom
                                        >
                                            {cardData[3].description}
                                        </StyledTypography>
                                    </div>
                                </SyledCardContent>
                                <Author authors={cardData[3].authors} />
                            </SyledCard>
                            <SyledCard
                                variant="outlined"
                                onFocus={() => handleFocus(4)}
                                onBlur={handleBlur}
                                tabIndex={0}
                                className={focusedCardIndex === 4 ? 'Mui-focused' : ''}
                                sx={{ height: '100%' }}
                            >
                                <SyledCardContent
                                    sx={{
                                        display: 'flex',
                                        flexDirection: 'column',
                                        justifyContent: 'space-between',
                                        height: '100%',
                                    }}
                                >
                                    <div>
                                        <Typography gutterBottom variant="caption" component="div">
                                            {cardData[4].tag}
                                        </Typography>
                                        <Typography gutterBottom variant="h6" component="div">
                                            {cardData[4].title}
                                        </Typography>
                                        <StyledTypography
                                            variant="body2"
                                            color="text.secondary"
                                            gutterBottom
                                        >
                                            {cardData[4].description}
                                        </StyledTypography>
                                    </div>
                                </SyledCardContent>
                                <Author authors={cardData[4].authors} />
                            </SyledCard>
                        </Box>
                    </Grid>
                    <Grid size={{ xs: 12, md: 4 }}>
                        <SyledCard
                            variant="outlined"
                            onFocus={() => handleFocus(5)}
                            onBlur={handleBlur}
                            tabIndex={0}
                            className={focusedCardIndex === 5 ? 'Mui-focused' : ''}
                            sx={{ height: '100%' }}
                        >
                            <CardMedia
                                component="img"
                                alt="green iguana"
                                image={cardData[5].img}
                                sx={{
                                    height: { sm: 'auto', md: '50%' },
                                    aspectRatio: { sm: '16 / 9', md: '' },
                                }}
                            />
                            <SyledCardContent>
                                <Typography gutterBottom variant="caption" component="div">
                                    {cardData[5].tag}
                                </Typography>
                                <Typography gutterBottom variant="h6" component="div">
                                    {cardData[5].title}
                                </Typography>
                                <StyledTypography variant="body2" color="text.secondary" gutterBottom>
                                    {cardData[5].description}
                                </StyledTypography>
                            </SyledCardContent>
                            <Author authors={cardData[5].authors} />
                        </SyledCard>
                    </Grid>
                </Grid>
                <Grid container spacing={2} columns={12}>
                    <Grid size={{ xs: 12, md: 9 }}>
                        <SyledCard
                            variant="outlined"
                            onFocus={() => handleFocus(0)}
                            onBlur={handleBlur}
                            tabIndex={0}
                            className={focusedCardIndex === 0 ? 'Mui-focused' : ''}
                        >
                            <CardMedia
                                component="img"
                                alt="green iguana"
                                image={cardData[0].img}
                                sx={{
                                    aspectRatio: '16 / 9',
                                    borderBottom: '1px solid',
                                    borderColor: 'divider',
                                }}
                            />
                            <SyledCardContent>
                                <Typography gutterBottom variant="caption" component="div">
                                    {cardData[0].tag}
                                </Typography>
                                <Typography gutterBottom variant="h6" component="div">
                                    {cardData[0].title}
                                </Typography>
                                <StyledTypography variant="body2" color="text.secondary" gutterBottom>
                                    {cardData[0].description}
                                </StyledTypography>
                            </SyledCardContent>
                            <Author authors={cardData[0].authors} />
                        </SyledCard>
                    </Grid>
                    <Grid size={{  md: 3 }}>




                    </Grid>
                </Grid>
            </Box>


















        </div>
    );
};

export default PostList;
