import * as React from 'react';
import PropTypes from 'prop-types';
import Avatar from '@mui/material/Avatar';
import AvatarGroup from '@mui/material/AvatarGroup';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Chip from '@mui/material/Chip';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';

const cardData = [
    {
        img: 'https://picsum.photos/800/450?random=1',
        tag: 'Engineering',
        title: 'Revolutionizing software development with cutting-edge tools',
        description:
            'Our latest engineering tools are designed to streamline workflows and boost productivity.',
        authors: [
            { name: 'Remy Sharp', avatar: '/static/images/avatar/1.jpg' },
            { name: 'Travis Howard', avatar: '/static/images/avatar/2.jpg' },
        ],
    },
    {
        img: 'https://picsum.photos/800/450?random=2',
        tag: 'Design',
        title: 'Exploring innovative design principles for 2024',
        description: 'Learn about the latest trends and strategies in the world of design.',
        authors: [
            { name: 'Alice Brown', avatar: '/static/images/avatar/3.jpg' },
            { name: 'Jake Paul', avatar: '/static/images/avatar/4.jpg' },
        ],
    },
];

const categories = ['All Categories', 'Engineering', 'Design', 'Technology', 'Health', 'Education'];

const StyledCard = styled(Card)(({ theme }) => ({
    display: 'flex',
    flexDirection: 'column',
    padding: 0,
    height: '100%',
    backgroundColor: (theme.vars || theme).palette.background.paper,
    '&:hover': {
        backgroundColor: 'transparent',
        cursor: 'pointer',
    },
}));

const StyledCardContent = styled(CardContent)(() => ({
    display: 'flex',
    flexDirection: 'column',
    gap: 4,
    padding: 16,
    flexGrow: 1,
    '&:last-child': {
        paddingBottom: 16,
    },
}));

const StyledTypography = styled(Typography)(() => ({
    display: '-webkit-box',
    WebkitBoxOrient: 'vertical',
    WebkitLineClamp: 2,
    overflow: 'hidden',
    textOverflow: 'ellipsis',
}));

function Author({ authors }) {
    return (
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <AvatarGroup max={3}>
                {authors.map((author, index) => (
                    <Avatar key={index} alt={author.name} src={author.avatar} sx={{ width: 24, height: 24 }} />
                ))}
            </AvatarGroup>
            <Typography variant="caption">
                {authors.map((author) => author.name).join(', ')}
            </Typography>
        </Box>
    );
}

Author.propTypes = {
    authors: PropTypes.arrayOf(
        PropTypes.shape({
            avatar: PropTypes.string.isRequired,
            name: PropTypes.string.isRequired,
        }),
    ).isRequired,
};

export default function MainContent() {
    const [selectedCategory, setSelectedCategory] = React.useState('All Categories');
    const [searchText, setSearchText] = React.useState('');

    const handleCategoryClick = (category) => {
        setSelectedCategory(category);
    };

    const handleSearchChange = (event) => {
        setSearchText(event.target.value);
    };

    const filteredCards = cardData.filter(
        (card) =>
            (selectedCategory === 'All Categories' || card.tag === selectedCategory) &&
            (card.title.toLowerCase().includes(searchText.toLowerCase()) ||
                card.description.toLowerCase().includes(searchText.toLowerCase()))
    );

    return (
        <Box sx={{ display: 'flex', flexDirection: 'row', gap: 2, width: '100%' }}>
            {/* Main Content */}
            <Box sx={{ width: '75%', padding: 2 }}>
                <Grid container spacing={2} columns={12}>
                    {filteredCards.map((card, index) => (
                        <Grid item xs={12} key={index}>
                            <StyledCard variant="outlined">
                                <CardMedia
                                    component="img"
                                    alt={card.title}
                                    image={card.img}
                                    sx={{
                                        aspectRatio: '16 / 9',
                                        borderBottom: '1px solid',
                                        borderColor: 'divider',
                                    }}
                                />
                                <StyledCardContent>
                                    <Typography gutterBottom variant="caption">
                                        {card.tag}
                                    </Typography>
                                    <Typography gutterBottom variant="h6">
                                        {card.title}
                                    </Typography>
                                    <StyledTypography variant="body2">{card.description}</StyledTypography>
                                </StyledCardContent>
                                <Box sx={{ padding: 2 }}>
                                    <Author authors={card.authors} />
                                </Box>
                            </StyledCard>
                        </Grid>
                    ))}
                </Grid>
            </Box>

            {/* Sidebar */}
            <Box
                sx={{
                    width: '25%',
                    display: 'flex',
                    flexDirection: 'column',
                    gap: 2,
                    padding: 2,
                    backgroundColor: 'background.default',
                    borderLeft: '1px solid',
                    borderColor: 'divider',
                }}
            >
                <TextField
                    fullWidth
                    label="Search"
                    variant="outlined"
                    value={searchText}
                    onChange={handleSearchChange}
                />
                <Typography variant="h6" gutterBottom>
                    Categories
                </Typography>
                {categories.map((category, index) => (
                    <Chip
                        key={index}
                        label={category}
                        onClick={() => handleCategoryClick(category)}
                        color={selectedCategory === category ? 'primary' : 'default'}
                        clickable
                        sx={{
                            justifyContent: 'start',
                            borderRadius: 0, // No rounded design
                            padding: '8px',
                            border: '1px solid',
                            borderColor: 'divider',
                        }}
                    />
                ))}
            </Box>
        </Box>
    );
}
