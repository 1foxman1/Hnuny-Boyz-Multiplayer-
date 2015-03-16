using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;
using System.Text;

namespace WindowsGame1
{
    public class Block
    {
        private int x;
        private int y;
        private int width;
        private int height;

        private Texture2D texture;
        private Rectangle location;

        public Block(int x, int y)
        {
            this.x = x;
            this.y = y;
            this.width = 250;
            this.height = 250;
        }

        public void LoadContent(ContentManager Content)
        {
            this.texture = Content.Load<Texture2D>("hungary");
            this.location = new Rectangle(this.x, this.y, this.width, this.height);
        }

        public void Draw(SpriteBatch spriteBatch)
        {
            spriteBatch.Draw(this.texture, this.location, null, Color.White, 0, new Vector2(0, 0), SpriteEffects.None, 1);
        }

        public Rectangle Location
        {
            get { return this.location; }
        }

        public int X
        {
            get { return this.location.X; }
            set { this.location.X = value; }
        }

        public int Y
        {
            get { return this.location.Y; }
            set { this.location.Y = value; }
        }
    }
}
